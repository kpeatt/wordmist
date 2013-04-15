# core/views.py
from django.views.generic.detail import SingleObjectMixin

from braces.views import JSONResponseMixin

class ObjectApiMixin(JSONResponseMixin, SingleObjectMixin):
    
    @property
    def model(self):
        msg = "model needs to be defined for ObjectApiView"
        raise NotImplementedError(msg)
    
    @property
    def form_class(self):
        msg = "form_class not defined for ObjectApiView"
        raise NotImplementedError(msg)
    
    def get(self, *args, **kwargs):
        """ Returns a single JSON object in a JSON list
            representing the model instance
        """
        instance = [self.get_object()]
        return self.render_json_object_response(instance)
    
    def post(self, *args, **kwargs):
        """ Updates a single object.
            If successful, returns 200 and serialized instance.
            If not, returns 400 and serialized form errors.
        """
        instance = self.get_object()
        
        form = self.form_class(self.request.POST,
                        instance=instance)
        if form.is_valid():
            instance = form.save()
            return self.render_json_object_response([instance])
        
        response = self.render_json_response(form.errors)
        response.status_code = 400
        return response