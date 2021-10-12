from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FindVacancyForm
from .models import City, Specialty
from .scraping_services.get_vacancies import get_vacancies


def index(request):
    form = FindVacancyForm
    return render(request, 'find_job/home.html', {'form': form})


def list_view(request):
    form = FindVacancyForm()
    city = request.GET.get('city')
    specialty = request.GET.get('specialty')
    vacancies = get_vacancies(specialty=specialty, city=city)
    context = {
        'city': city,
        'specialty': specialty,
        'city_name': City.objects.filter(slug=city).first(),
        'specialty_name': Specialty.objects.filter(slug=specialty).first(),
        'jobs_num': len(vacancies),
        'form': form,
    }
    if vacancies:
        paginator = Paginator(vacancies, 20)
        page_number = request.GET.get('page')
        try:
            vacancies = paginator.page(page_number)
        except PageNotAnInteger:
            vacancies = paginator.page(1)
        except EmptyPage:
            vacancies = paginator.page(paginator.num_pages)
    context['jobs'] = vacancies
    return render(request, 'find_job/list.html', context)

