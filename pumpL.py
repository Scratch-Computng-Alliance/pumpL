import requests

def RetrivePopularProjects():
  url = "https://api.scratch.mit.edu/studios/35370452/projects"
  response = requests.get(url)
  if response.status_code == 200:
    projects = response.json
    PopularProjects = sorted(projects, key=lambda x: x['stats']['views'], reverse=True)[:limit]
    print(f"Top {limit} Popular Projects in Studio {studio_id}:\n")
    for i, project in enumerate(popular_projects, start=1):
      title = project['title']
      author = project['author']['username']
      views = project['stats']['views']
      print(f"{i}. {title} by {author} - Views: {views}")
  else:
      print(f"Failed to retrieve projects. Status code: {response.status_code}")
