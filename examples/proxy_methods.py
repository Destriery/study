from typing import Callable, Optional

"""Usage

class CustomClass(ClassWithProxy):
    proxy_methods = {
        'original_method': 'some_property.target_method'
    }

    some_property = AnotherClass()

-------------------

_obj = CustomClass()

assert _obj.original_method == some_property.target_method

"""


# Proxy original methods to service methods. `{'list_documents': 'service.documents.list_documents'}`
ProxyMethods = dict[str, str]


class ClassWithProxy:
    proxy_methods: Optional[ProxyMethods] = None

    def __init__(self) -> None:
        self._set_proxy_methods()

    def _set_proxy_methods(self):
        if not self.proxy_methods: return None

        vaild_proxy_methods = {}
        for original_method, target_method in self.proxy_methods.items():
            current_attribute = self
            for attribute in target_method.split('.'):
                current_attribute = getattr(current_attribute, attribute, None)

                if not current_attribute: break

            if current_attribute and callable(current_attribute):
                vaild_proxy_methods[original_method] = current_attribute

        self.__dict__.update(vaild_proxy_methods)


class ClassWithProxyViaGetAttr:
    proxy_methods: Optional[ProxyMethods] = None

    def __init__(self) -> None:
        ...

    def __getattr__(self, method_name: str) -> Callable:
        """It uses to proxy methods to managers"""
        try:
            current_attribute = None

            if self.proxy_methods:
                target_method = self.proxy_methods.get(method_name)

                if not target_method: raise AttributeError

                current_attribute = self
                for attribute in target_method.split('.'):
                    current_attribute = getattr(current_attribute, attribute, None)

                    if not current_attribute: raise AttributeError

            if not callable(current_attribute): raise AttributeError

            return current_attribute

        except AttributeError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{method_name}'")
