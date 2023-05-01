class FileTest:
    # __init__ currently not in use for a single image upload
    def __init__( self, data ):
        self.id = data['id']
        self.file_name = data['file_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # adds file name to cars table
    @classmethod
    def save( cls, data ):
        query = """
        INSERT INTO cars (file_name) 
        VALUES (%(file_name)s);
        """

        return connectToMySQL( cls.db ).query_db( query, data )