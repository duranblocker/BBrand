from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post, Svg, SvgPath
from users.models import Profile

def parameters(request):
	if request.method == 'POST':
		Svg_form = SvgUpdateForm(request.POST, instance=request.title)
		SvgPath_form = SvgPathUpdateForm(request.POST, request.FILES, instance=request.title.Svg)
		if Svg_form.is_valid() and SvgPath_form.is_valid():
			Svg_form.save()
			SvgPath_form.save()
			messages.success(request, f'Your account has been Updated!')
			return render(request, 'svg_list.html', {})

	else:
		Svg_form = SvgUpdateForm(instance=request.title)
		SvgPath_form = SvgPathUpdateForm(instance=request.title.Svg)
		return render(request, 'svg_list.html')

def user(request):
	if request.method == "POST":
		nameid = request.POST['userid']
		context = {
			'puser': Profile.objects.filter(user_id= int(nameid)),
			'posts': Post.objects.filter(name_id= int(nameid)),
		}
		return render(request, 'user.html', context)

	return render(request, 'user.html', {})
		
 
def home(request):
	context = {
		'posts': Post.objects.all(),
	}
	return render(request, 'home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.name:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.name:
			return True
		return False


class SvgUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Svg
	fields = ['title', 'wallType', 'wallRefNum', 'path', 'width', 'height']

	def form_valid(self, form):
		form.instance.title = self.request.title
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.title == post.title:
			return True
		return False

class SvgPathListView(ListView):
	model = SvgPath
	fields = ['title','startx', 'starty', 'linetype','PathRefNum','endx','endy','data1', 'data2','data3','data4','data5','data6','data7','data8','data9']
	ordering = ['PathRefNum']
	
	def form_valid(self, form):
		form.instance.title = self.request.title
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.title == Svg.title:
			return True
		return False

def about(request):
	return render(request, 'about.html', {'title': 'About'})
		

def parameters(request):
	if request.method == 'POST':
		Svg_form = SvgUpdateForm(request.POST, instance=request.title)
		SvgPath_form = SvgPathUpdateForm(request.POST, request.FILES, instance=request.title.Svg)
		if Svg_form.is_valid() and SvgPath_form.is_valid():
			Svg_form.save()
			SvgPath_form.save()
			messages.success(request, f'Your account has been Updated!')
			return render(request, 'svg_list.html', {})

	else:
		Svg_form = SvgUpdateForm(instance=request.title)
		SvgPath_form = SvgPathUpdateForm(instance=request.title.Svg)


# def parameters(request):
#	return render(request, 'svg_list.html', {})"""


	

 