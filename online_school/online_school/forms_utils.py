from django import forms

def apply_bootstrap_classes(form):
    for field in form.fields.values():
        widget = field.widget

        if isinstance(widget, forms.CheckboxInput):
            widget.attrs["class"] = "form-check-input"
        elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
            widget.attrs["class"] = "form-select"
        elif isinstance(widget, forms.Textarea):
            widget.attrs["class"] = "form-control"
            widget.attrs.setdefault("rows", 4)
        else:
            widget.attrs["class"] = "form-control"
