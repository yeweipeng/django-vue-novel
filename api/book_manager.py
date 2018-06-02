from .models import BookLikeTab

def get_like_book_list(user_id):
  return list(BookLikeTab.objects.filter(user_id=user_id, flag=1).values())
