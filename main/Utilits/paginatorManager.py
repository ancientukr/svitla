class PaginatorManager():

    def next(self, Album, album_id):
        try:
            n = Album.objects.get(id=album_id).get_next_by_data().id
        except Exception:
            return 0
        if Album.objects.get(id=album_id).get_next_by_data().categories == Album.objects.get(id=album_id).categories:
            return n
        else:
            self.next(Album, n)

    def previous(self, Album, album_id):
        try:
            n = Album.objects.get(id=album_id).get_previous_by_data().id
        except Exception:
            return 0
        if Album.objects.get(id=album_id).get_previous_by_data().categories == Album.objects.get(id=album_id).categories:
            return n
        else:
            self.next(Album, n)