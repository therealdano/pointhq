# -*- coding: utf-8 -*-

class ZoneError(Exception):
    pass

class BaseItem(object):

    # BaseItem is an abstract for the basic API single resource response, i.e.
    # { "zone": {"key": "value"}}. 

    def __init__(self, resource_r):
        if isinstance(resource_r, dict) == False:
            raise TypeError("BaseItem requires a dictionary")

        self.resource_r = resource_r
        self.isstatus = False
        self.verify()

    def verify(self):

        # The API resource response should contain either `zone` or 
        # `zone_record`. If neither are present, none of the following
        # convenience classes wil be of any use
        if (self.resource_r.__contains__("zone") == False 
                and self.resource_r.__contains__("zone_record") == False):
            raise ZoneError("Resource response missing `zone` or `zone_record`")

        # If the resource response contains `zone` then this is a zone item
        # so we simply set the base to the `zone` key
        if self.resource_r.__contains__("zone"):
            self.item_class = "Zone"
            self.base = self.resource_r["zone"]

        # If the resource response contains `zone_record` then this is a 
        # zone record items and the base is set to the `zone_record` key
        if self.resource_r.__contains__("zone_record"):
            self.item_class = "ZoneRecord"
            self.base = self.resource_r["zone_record"]

        # Finally, check if the item is a status notification (this would
        # be true if the resource is from a HTTP DELETE) and set isstatus
        # appropriately
        if self.base.__contains__("status"):
            self.isstatus = True
        else:
            # As long as we're here, check that there's an `id` key. If not
            # raise an error because nothing else is going to work
            if not self.base.__contains__("id"):
                raise ZoneError(
                        "Resource response missing `zone` or `zone_record`")
            
class Zone(BaseItem):

    # Zone is an abstract for basic zone items. This may include only one

    # method, status, if generated from a DELETE request
    
    @property
    def status(self):
        if self.isstatus:
            return self.base["status"]
        return None

    @property
    def id(self):
        if not self.isstatus:
            return self.base["id"]
        return None

    @property
    def name(self):
        if not self.isstatus:
            return self.base["name"]
        return None

    @property
    def group(self):
        if not self.isstatus:
            return self.base["group"]
        return None

    @property
    def user_id(self):
        if not self.isstatus:
            return self.base["user-id"]
        return None

    @property
    def ttl(self):
        if not self.isstatus:
            return self.base["ttl"]
        return None


class ZoneRecord(BaseItem):

    # ZoneRecord is an abstract for zone records. As with Zone it may contain
    # only the status method when loaded from DELETE resources

    @property
    def status(self):
        if self.isstatus:
            return self.base["status"]
        return None

    @property
    def id(self):
        if not self.isstatus:
            return self.base["id"]
        return None

    @property
    def name(self):
        if not self.isstatus:
            return self.base["name"]
        return None

    @property
    def ttl(self):
        if not self.isstatus:
            return self.base["ttl"]
        return None

    @property
    def zone_id(self):
        if not self.isstatus:
            return self.base["zone_id"]
        return None

    @property
    def data(self):
        if not self.isstatus:
            return self.base["data"]
        return None

    @property
    def aux(self):
        if not self.isstatus:
            return self.base["aux"]
        return None

    @property
    def record_type(self):
        if not self.isstatus:
            return self.base["record_type"]
        return None

    @property
    def redirect_to(self):
        if not self.isstatus:
            return self.base["redirect_to"]
        return None
