from app import db
 
########################################################################
class User(db.Model):
    """"""
    __tablename__ = "Users"
 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), nullable = False, unique= True)
    username = db.Column(db.String(25), nullable = False, unique= True)
    password = db.Column(db.String(256), nullable = False)
    level = db.Column(db.Integer, nullable = False)
    authenticated = db.Column(db.Boolean, default =False)
    dob = db.DATE()
    gender = db.Column(db.String(1))
    create_time = db.DATETIME()


 
    #----------------------------------------------------------------------
    # User functions
    #----------------------------------------------------------------------

    # Input: string of email, username, and password required. Integer for access level
    # Description: defualt constructor for User class
    def __init__(self, email, username, password, level):
        """"""
        self.email = email
        self.username = username
        self.password = password
        self.level = level

    # Input: none
    # Output: returns boolean of login authentication
    # Description: To authenticate user for login_manager
    def is_authenticated(self):
        return self.authenticated

    # Input: none
    # Output: returns boolean
    # Description: Active user for login_manager
    def is_active(self):
        return True

    # Input: none
    # Output: returns boolean
    # Description: For anonymous logins for login_manager
    def is_anonymous(self):
        return False

    # Input: none
    # Output: returns string
    # Description: ID for login_manager
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return ("<User {}>".format(self.username))
 
# create tables
#Base.metadata.create_all(engine)
