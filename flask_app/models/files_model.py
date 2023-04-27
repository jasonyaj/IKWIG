class FileTest:
    # __init__ currently not in use for a single image upload
    def __init__( self, data ):
        self.id = data['id']
        self.file_name = data['file_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save( cls, data ):
        query = """
        INSERT INTO cars (file_name) 
        VALUES (%(file_name)s);
        """

        return connectToMySQL( cls.db ).query_db( query, data )


    # cuurently this mehtod is not in use
    @classmethod
    def get_one_by_id( cls, data ):
        query = """
        SELECT * FROM files WHERE id = %(id)s;
        """

        results = connectToMySQL( cls.db ).query_db( query, data )

        return FileTest(results[0])
    

    # cuurently this mehtod is not in use
    @classmethod
    def get_all( cls ):
        query = 'SELECT * from files'

        results = connectToMySQL( cls.db ).query_db( query )

        files = []

        for row in results:
            files.append(cls(row))

        return files
