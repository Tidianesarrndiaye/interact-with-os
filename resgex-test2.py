import re


def secure_website_domain(website):
 pattern = r"^https://www.([\w.-]+)\.co[m]?$" # enter the regex pattern here
 result = re.search(pattern, website) # enter the re method here
 if result is None:
  return ""
 return  result[1] # enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text


print("\n")
print("-"*50)


def find_isbn(list):
  pattern = r"\b(\d{3})-(\d{1})-(\d{2})-(\d{6})-(\d{1})\b" #enter the regex pattern here
  result = re.search(pattern, list) #enter the re method  here
  if result is None:
    return ""
  return result[4] #return the correct capturing group


print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank

print("\n")
print("-"*50)

