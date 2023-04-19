import io
import json
def postAttach(blog_name, image_url):
   url = "https://www.tistory.com/apis/post/attach?"
   url += "access_token=" + input_data['access_token'] + "&"
   url += "blogName=" + blog_name + "&"
   url += "targetUrl=" + blog_name + "&"
   url += "output=json"


   # 이미지 URL 다운로드
   response = requests.get(image_url)
   file_obj = io.BytesIO(response.content)
   # 업로드할 파일 설정
   files = {"uploadedfile": file_obj}


   res = requests.post(url, files=files).content
   result = json.loads(res)
      
   uploaded_file_url = result['tistory']['url']
   uploaded_file_replacer = result['tistory']['replacer']
   print("uploaded_file_replacer : ", uploaded_file_replacer)


   return uploaded_file_replacer


def postWrite(blog_name, title, content="", visibility=None, category_id=None, published=None, slogan=None, tag=None,
             acceptComment=None, password=None, output_type="json",image_main_url=None):
   url = "https://www.tistory.com/apis/post/write?"
   data = {}
   data['access_token'] = input_data['access_token']
   data['output'] = output_type
   data['blogName'] = blog_name
   data['title'] = title
   if image_main_url is not None:
     content += '<p>' + postAttach(blog_name,image_main_url) + '</p>'


   data['content'] = content
   #url += "access_token=" + access_token + "&"
   #url += "output=" + output_type + "&"
   #url += "blogName=" + blog_name + "&"
   #url += "title=" + title + "&"
   #url += "content=" + content + "&"
   if visibility is not None:
       url += "visibility=" + visibility + "&"
   if category_id is not None:
       url += "category=" + category_id + "&"
   if published is not None:
       url += "published=" + published + "&"
   if slogan is not None:
       url += "slogan=" + slogan + "&"
   if tag is not None:
       url += "tag=" + tag + "&"
       print(tag)
   if acceptComment is not None:
       url += "acceptComment=" + acceptComment + "&"
   if password is not None:
       url += "password=" + password
  
   res = requests.post(url, data=data).content
   print(res)




postWrite(input_data["blog_name"],input_data["title"],input_data["content"],input_data["visibility"],input_data["category_id"],None,None,input_data['tags'],None,None,"json",input_data["image_main_url"])


return {"text": "finish"}

