from django.shortcuts import render

dummy_posts = [
	{
		'title': "The Downfall of the Second",
		'author': "David Resmith",
		'date': "123rd August 2021",
		'content': "It was a cold morning yesterday. The last day of the year..."
	},
	{
		'title': "Top 2 Nightmares to Wake Up Screaming From",
		'author': "Phillip Chinowezechk",
		'date': "-02th Febranuary 2021",
		'content': "1. An elephant staring at you\n2. A dog staring at you"
	}
]

#handles traffic from homepage of blog
def home(request):
	context = {'posts': dummy_posts}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About Page'})