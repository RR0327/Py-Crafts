import os
import csv
from io import BytesIO
from django.shortcuts import render
from django.conf import settings
from django.core.files import File
from django.http import FileResponse, Http404, HttpResponse
from django.db import models
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6, letter
from reportlab.lib.units import mm
import barcode
from barcode.writer import ImageWriter
from .models import Product

def home_view(request):
    return render(request, 'barcodegen/home.html')

def generate_barcode(request):
    context = {}
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        code_type = request.POST['code_type']
        code_value = request.POST['code_value']

        try:
            barcode_class = barcode.get_barcode_class(code_type)
            barcode_obj = barcode_class(code_value, writer=ImageWriter())
            output_path = os.path.join(settings.MEDIA_ROOT, 'barcodes')
            os.makedirs(output_path, exist_ok=True)
            filename = f"{code_type}_{code_value}"
            full_path = barcode_obj.save(os.path.join(output_path, filename))

            product = Product(
                name=name,
                description=description,
                price=price,
                code_type=code_type,
                code_value=code_value
            )
            with open(full_path, 'rb') as f:
                product.barcode_image.save(f"{filename}.png", File(f), save=True)

            context['success'] = True
            context['barcode_image'] = product.barcode_image

        except Exception as e:
            context['error'] = str(e)

    return render(request, 'barcodegen/home.html', context)

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(code_type__icontains=query) |
            models.Q(code_value__icontains=query)
        ).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')

    return render(request, 'barcodegen/product_list.html', {
        'products': products,
        'query': query
    })

def upload_csv(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            context['error'] = "File is not CSV."
            return render(request, 'barcodegen/upload_csv.html', context)

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                name = row['name']
                description = row.get('description', '')
                price = row['price']
                code_type = row['code_type']
                code_value = row['code_value']

                try:
                    barcode_class = barcode.get_barcode_class(code_type)
                    barcode_obj = barcode_class(code_value, writer=ImageWriter())
                    output_path = os.path.join(settings.MEDIA_ROOT, 'barcodes')
                    os.makedirs(output_path, exist_ok=True)
                    filename = f"{code_type}_{code_value}"
                    full_path = barcode_obj.save(os.path.join(output_path, filename))

                    product = Product(
                        name=name,
                        description=description,
                        price=price,
                        code_type=code_type,
                        code_value=code_value
                    )
                    with open(full_path, 'rb') as f:
                        product.barcode_image.save(f"{filename}.png", File(f), save=True)

                except Exception as e:
                    print(f"Error in row {row}: {e}")

            context['success'] = "CSV uploaded and barcodes generated successfully."
        except Exception as e:
            context['error'] = f"Error processing file: {e}"

    return render(request, 'barcodegen/upload_csv.html', context)

def download_png(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        return FileResponse(product.barcode_image, as_attachment=True, filename=product.barcode_image.name)
    except Product.DoesNotExist:
        raise Http404("Barcode not found.")

def download_pdf(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A6)
        p.setFont("Helvetica-Bold", 12)
        p.drawString(10 * mm, 90 * mm, f"Product: {product.name}")
        p.setFont("Helvetica", 10)
        p.drawString(10 * mm, 83 * mm, f"Price: ${product.price}")
        p.drawString(10 * mm, 76 * mm, f"Code: {product.code_type} - {product.code_value}")
        p.drawString(10 * mm, 69 * mm, f"Description: {product.description[:50]}...")
        if product.barcode_image:
            p.drawImage(product.barcode_image.path, 10 * mm, 20 * mm, width=70 * mm, height=35 * mm)
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f"{product.name}_label.pdf")
    except Product.DoesNotExist:
        raise Http404("Product not found.")

def export_products_csv(request):
    products = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Description', 'Price', 'Code Type', 'Code Value'])

    for p in products:
        writer.writerow([p.name, p.description, p.price, p.code_type, p.code_value])

    return response

def export_products_pdf(request):
    products = Product.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="products.pdf"'

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    y = 750
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(30, y, "Product List")
    y -= 30

    pdf.setFont("Helvetica", 10)
    for p in products:
        text = f"{p.name} | {p.code_type}: {p.code_value} | ${p.price}"
        pdf.drawString(30, y, text)
        y -= 20
        if y < 50:
            pdf.showPage()
            y = 750

    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="products.pdf")
