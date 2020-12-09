from pafy import new
url = input('ENTER YOUR LINK HERE: ')
video = new(url)
dl = video.getbest()
dl.download()