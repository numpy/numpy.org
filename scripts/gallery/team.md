<div>
  <img src="../images/logo.svg" alt="NumPy Logo" width="75">
</div>

# NumPy Team Gallery

We are an international team on a mission to support scientific and research communities worldwide by building quality, open-source software. [**Join us**](/contribute)!

<hr>

###Maintainers

<div class="row maintainers">
    {% for row in main.maintainers.people | batch(9, "") %}
        <div class="card-group maintainers">
        {% for person in row %}
            {% if person %}
                <div class="card rounded" style="border: 0;">
                    <img class="card-img-top" style="padding: 0.25rem; border-radius: 10%;" alt="" src="{{ person.avatar_url }}"/>
                    <div style="padding-bottom: 0;" class="card-body">
                        <div style="padding: 0; font-size: 0.8rem" class="card-title small"> {{ person.name or person.login }} </div>
                        <div style="padding: 0; font-size: 0.5rem" class="text-muted small"> {{ person.company }} </div>
                        <a style="padding: 0; font-size: 0.5rem;" class="card-footer small" href="{{ person.html_url }}">{{ person.login }}</a>
                    </div>
                </div>
            {% else %}
                <div class="card border-0 bg-light"></div>
            {% endif %}
        {% endfor %}
    </div>
    <div></div>
  {% endfor %}
</div>
<div></div>
<hr>

### Web Team

<div class="row maintainers">
    {% for row in main.maintainers.webpeople | batch(9, "") %}
        <div class="card-group maintainers">
        {% for person in row %}
            {% if person %}
                <div class="card rounded" style="border: 0;">
                    <img class="card-img-top" style="padding: 0.25rem; border-radius: 10%;" alt="" src="{{ person.avatar_url }}"/>
                    <div style="padding-bottom: 0;" class="card-body">
                        <div style="padding: 0; font-size: 0.8rem" class="card-title small"> {{ person.name or person.login }} </div>
                        <div style="padding: 0; font-size: 0.5rem" class="text-muted small"> {{ person.company }} </div>
                        <a style="padding: 0; font-size: 0.5rem;" class="card-footer small" href="{{ person.html_url }}">{{ person.login }}</a>
                    </div>
                </div>
            {% else %}
                <div class="card border-0 bg-light"></div>
            {% endif %}
        {% endfor %}
    </div>
  {% endfor %}
</div>
<hr>

### Documentation Team

<div class="row maintainers">
    {% for row in main.maintainers.docpeople | batch(9, "") %}
        <div class="card-group maintainers">
        {% for person in row %}
            {% if person %}
                <div class="card rounded" style="border: 0;">
                    <img class="card-img-top" style="padding: 0.25rem; border-radius: 10%;" alt="" src="{{ person.avatar_url }}"/>
                    <div style="padding-bottom: 0;" class="card-body">
                        <div style="padding: 0; font-size: 0.8rem" class="card-title small"> {{ person.name or person.login }} </div>
                        <div style="padding: 0; font-size: 0.5rem" class="text-muted small"> {{ person.company }} </div>
                          <a style="padding: 0; font-size: 0.5rem;" class="card-footer small" href="{{ person.html_url }}">{{ person.login }}</a>
                    </div>
                </div>
            {% else %}
                <div class="card border-0 bg-light"></div>
            {% endif %}
        {% endfor %}
    </div>
  {% endfor %}
</div>
<hr>

### Emeritus maintainers

<div class="emeritus">
    {% for row in main.maintainers.emerpeople | batch(9, "") %}
        <div class="card-group emerpeople">
        {% for person in row %}
            {% if person %}
                <div class="card rounded" style="border: 0;">
                    <img class="card-img-top" style="padding: 0.25rem; border-radius: 10%; filter: grayscale(100%);" alt="" src="{{ person.avatar_url }}"/>
                    <div style="padding-bottom: 0;" class="card-body">
                        <div style="padding: 0; font-size: 0.8rem" class="card-title text-muted small"> {{ person.name or person.login }} </div>
                        <div style="padding: 0; font-size: 0.5rem" class="text-muted small"> {{ person.company }} </div>
                        <a style="padding: 0; font-size: 0.5rem;" class="card-footer small" href="{{ person.html_url }}">{{ person.login }}</a>
                    </div>
                </div>
            {% else %}
                <div class="card border-0 bg-light"></div>
            {% endif %}
        {% endfor %}
    </div>
  {% endfor %}
</div>

### Governance

For the list of the Steering Council members, please see [here](https://numpy.org/about/).
