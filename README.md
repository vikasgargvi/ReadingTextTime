# ReadingTextTime

# ALSO MAKE ENTRIES IN

Place this file in the same directory where is views.py

** models.py --> class Post

	avg_time = models.CharField(max_length = 40, default='')

** views.py --> class in which you store post in database

// import

	from .ReadingTime import CalculateTime
	
  //add before saving post in database
  
    	post.avg_time = CalculateTime.calTime(post.text)
