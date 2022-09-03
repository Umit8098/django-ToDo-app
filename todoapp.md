- py -m venv env
- ./env/Scripts/activate
- py manage.py runserver
- pip install django
- python.exe -m pip install --upgrade pip
- 7 pip freeze
- 8 pip freeze > requirements.txt
- 2 django-admin startproject main .
- 3 pip install python-decouple
- pip freeze > requirements.txt



{{ form.as_div }} will render them wrapped in <div> tags.
{{ form.as_table }} will render them as table cells wrapped in <tr> tags.
{{ form.as_p }} will render them wrapped in <p> tags.
{{ form.as_ul }} will render them wrapped in <li> tags.


emoji ekleme win + .
emoji ekleme win + ;


<timeout.js> ->

```
let element = document.querySelector('.message');

setTimeout(function () {
  element.style.display = 'none';
}, 3000);
```

<script src="{% static 'todo/js/timeout.js' %}"></script>





en son template kodları:


```
{% extends 'todo/base.html' %} 


{% block content %}

<div>
    <div class="container pt-4">
        <div class="row mt-2 p-0">
            <div class="col-lg-4 mx-auto p-0 shadow">
                <div class="alert alert-warning text-center">
                    <h2>Add ToDo</h2>
                </div>
                <div class="p-4">
                    <form action="/add/" method="POST">
                        {% csrf_token%} {{form.as_p}}
                        <hr>
                        <input type="submit" value="ADD" class="btn btn-success">
                    </form>
                </div>
            </div>

            <div class="col">
                <div class="border">
                    {% if todos|length == 0 %}
                    <div class="p-4">
                        <br>
                        <br>
                        <div class="alert alert-danger text-center">
                            <p class="" style="font-size: 30px;">ToDo Lists</p>
                        </div>
                        <br>
                        <br>
                    </div>
                    {%else%}
                    <div class="p-2">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>No</th>
                                    <th>Title</th>
                                    <th>Status</th>
                                    <th>Priority</th>
                                    <th>Delete</th>
                                    <th>Update</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for todo in todos%}
                                <tr>
                                    <td>{{forloop.counter}}</td>
                                    <td>{{todo.title}}</td>
                                    {% if todo.status == 'C'%}
                                    <td>
                                        ✅
                                    </td>
                                    {% elif todo.status == 'I'%}
                                    <td>
                                        🚧
                                    </td>
                                    {% elif todo.status == 'P'%}
                                    <td>
                                        💤
                                    </td>
                                    {%endif%}

                                    <td>
                                        {% if todo.priority == '1'%}
                                            1️⃣
                                        {%elif todo.priority == '2'%}
                                            2️⃣
                                        {%elif todo.priority == '3'%}
                                            3️⃣
                                        {%elif todo.priority == '4'%}
                                            4️⃣
                                        {%elif todo.priority == '5'%}
                                            5️⃣
                                        {%endif%}
                                    </td>

                                    <td>
                                        <a href="delete/{{todo.id}}" title="Delete" class="">🗑️</a> 
                                    </td>
                                    <td>
                                            <a href="/update/{{todo.id}}"  class="">⚙️</a> 

                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                    {%endif%}
                </div>
            </div>
        </div>
    </div>



{% endblock content %}

```





```
{% extends 'todo/base.html' %}
{% block content %}



<div class="col-lg-4 mx-auto p-0 shadow">
    <div class="alert alert-warning text-center">
        <h2>Update ToDo</h2>
    </div>
    <div class="p-4 d-flex align-items-center ">
        <form action="" method="POST">
            {% csrf_token%} {{form.as_p}}
            <hr>
            <input type="submit" value="UPDATE" class="btn btn-success">
        </form>
    </div>
</div>


{% endblock content %}

```




```

body {
    background-image: url(https://cdn.pixabay.com/photo/2017/01/24/03/53/plant-2004483__480.jpg);
    background-size: cover;
    background-repeat: no-repeat;
}

```



style.css doyasına ekleyiniz:

```
textarea { max-width: 100% }
```

