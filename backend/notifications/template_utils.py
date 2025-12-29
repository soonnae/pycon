from jinja2 import Environment, Undefined, select_autoescape


class ShowPlaceholdersUndefined(Undefined):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.variable_name = kwargs.get("name")

    def __str__(self):
        return "{{" + self.variable_name + "}}"


def render_template_from_string(
    template_string: str, context: dict, *, show_placeholders: bool = False
) -> str:
    env = Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=select_autoescape(['html', 'xml'])
    )

    if show_placeholders:
        env.undefined = ShowPlaceholdersUndefined

    template = env.from_string(template_string)
    return template.render(context).strip()
