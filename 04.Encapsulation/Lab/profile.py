class Profile:
    min_username_length = 5
    max_username_length = 15

    min_password_length = 8
    min_uppercase_letters_count = 1
    min_digits_count = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if len(username) not in range(self.min_username_length, self.max_username_length + 1):
            raise ValueError(f"The username must be between {self.min_username_length} and {self.max_username_length} characters.")

    def __validate_password(self, password):
        error_message = f"The password must be {self.min_password_length} or more characters" \
                        f" with at least {self.min_digits_count} digit and {self.min_uppercase_letters_count} uppercase letter."

        if len(password) < self.min_password_length:
            raise ValueError(error_message)
        if len([x for x in password if x.isupper()]) < self.min_digits_count:
            raise ValueError(error_message)
        if len([x for x in password if x.isdigit()]) < self.min_uppercase_letters_count:
            raise ValueError(error_message)

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__validate_username(username)
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__validate_password(password)
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"".join(["*" for x in self.password])}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
print(correct_profile.username)