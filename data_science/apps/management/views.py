from django.shortcuts import render

# Обработка и ренден начального экрана
def main_page(request):
	return render(request, 'management/management-templates.html')