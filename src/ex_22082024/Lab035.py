# Match keyword

Browser_Name = input("Enter your browser name\n")
Browser_Name = Browser_Name.lower()
match Browser_Name:
    case "firefox":
        print("Execute the firfox code")
    case "chrome":
        print("Execute the chrome code")
    case "safari":
        print("Execute the Safari code")
    case _:
        print("Now browser found")
