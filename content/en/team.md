# NumPy Team Gallery

We are an international team on a mission to support scientific and research communities worldwide by building quality, open-source software. [**Join us**](/contribute)!

<hr>

###Maintainers

<div class="row maintainers">
    {% for row in main.maintainers.people | batch(9, "") %}
        <div class="card-group maintainers">
        {% for person in row %}
            {% if person %}
                <div class="card rounded">
                    <img class="card-img-top" style="border-radius: 5%;" alt="" src="{{ person.avatar_url }}"/>
                    <div class="card-body">
                        <h6 class="card-title">
                            {{ person.name or person.login }}
                        </h6>
                        <p class="card-text small">
                            <a href="{{ person.html_url }}">{{ person.login }}</a>
                        </p>
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

### Web Team

<div class="row maintainers">
    {% for row in main.maintainers.webpeople | batch(9, "") %}
        <div class="card-group maintainers">
        {% for person in row %}
            {% if person %}
                <div class="card rounded">
                    <img class="card-img-top" style="border-radius: 5%;" alt="" src="{{ person.avatar_url }}"/>
                    <div class="card-body">
                        <h6 class="card-title">
                            {{ person.name or person.login }}
                        </h6>
                        <p class="card-text small">
                            <a href="{{ person.html_url }}">{{ person.login }}</a>
                        </p>
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
                <div class="card rounded">
                    <img class="card-img-top" style="border-radius: 5%;" alt="" src="{{ person.avatar_url }}"/>
                    <div class="card-body">
                        <h6 class="card-title">
                            {{ person.name or person.login }}
                        </h6>
                        <p class="card-text small">
                            <a href="{{ person.html_url }}">{{ person.login }}</a>
                        </p>
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
                <div class="card rounded">
                    <img class="card-img-top" style="border-radius: 5%; filter: grayscale(100%);" alt="" src="{{ person.avatar_url }}"/>
                    <div class="card-body">
                        <h6 class="card-title">
                            {{ person.name or person.login }}
                        </h6>
                        <p class="card-text small">
                            <a href="{{ person.html_url }}">{{ person.login }}</a>
                        </p>
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

For the list of people on the Steering Council, please see [here](https://numpy.org/devdocs/dev/governance/people.html)
