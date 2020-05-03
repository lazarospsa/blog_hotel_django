from django.shortcuts import render

from hotel.models import Room, Booking
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.contrib.auth.models import User

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.

def home(request):
    return render(request, 'hotel/index.html')

def about(request):
    return render(request, 'hotel/about.html')

def thanks(request):
    return render(request, 'hotel/thanks.html')

class BookRoomView(DetailView):
    model = Booking

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['datein', 'dateout']

    def form_valid(self, form):
        form.instance.room_id = Room.objects.get(pk=self.kwargs.get('pk'))
        print(self.kwargs.get('pk'))
        form.instance.customer = self.request.user
        return super().form_valid(form)

        '''
    model = Room
    fields = ['title', 'description', 'price', 'maxpeople', 'tetragwnika', 'roomtypes', 'photoroom']
    
    def form_valid(self, form):
        return super().form_valid(form)
        '''

class RoomDetailView(DetailView):
    model = Room

class RoomSearchView(ListView):
    template_name = 'hotel/rooms.html'
    context_object_name = 'rooms'
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomSearchView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('searchroom')
        if query:
            return Room.objects.filter(title__icontains=query)
        else:
            return Room.objects.all()

class RoomListView(ListView):
    model = Room
    template_name = 'hotel/rooms.html'
    #<app>/<model>_<viewtype>.html <- auto psaxnei alla gia na to orisoume emeis diko mas template kanw template_name = 'blog/home.html'
    context_object_name = 'rooms'
    ordering = ['-price']
    #edw 9a valoume paginator (selidopoihsh)
    paginate_by = 4

@method_decorator(staff_member_required, name='dispatch')
class BookingsListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'hotel/list_bookings.html'
    #<app>/<model>_<viewtype>.html <- auto psaxnei alla gia na to orisoume emeis diko mas template kanw template_name = 'blog/home.html'
    context_object_name = 'bookings'
    ordering = ['-date_posted']
    #edw 9a valoume paginator (selidopoihsh)
    paginate_by = 4

@method_decorator(staff_member_required, name='dispatch')
class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['title', 'description', 'price', 'maxpeople', 'tetragwnika', 'roomtypes', 'photoroom']
    
    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(staff_member_required, name='dispatch')
class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Room
    fields = ['title', 'description', 'price', 'maxpeople', 'tetragwnika', 'roomtypes', 'photoroom']
    
    def form_valid(self, form):
        form.instance.room = self.request.user
        # ths formas o author = o user opou esteile to aithma (request)
        #running the form valid method, said the author befor send the form
        return super().form_valid(form)

    def test_func(self):#UserPassesTestMixin to test_func einai apo edw
        room = self.get_object() #vazoume to room se mia metavlhth
        return True #ean einai ontws epistrefei true ara to diagrafei

@method_decorator(staff_member_required, name='dispatch')
class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Room
    success_url = f'/hotel/rooms' #success_url einai proka9orismeno tou django

    def test_func(self):#UserPassesTestMixin to test_func einai apo edw
        room = self.get_object() #vazoume to room se mia metavlhth
        return True #ean einai ontws epistrefei true ara to diagrafei
