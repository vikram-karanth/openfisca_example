"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, ETERNITY
from openfisca_core.variables import Variable
from openfisca_core.indexed_enums import Enum

# Import the Entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import Shipment
import logging

# This variable is a pure input: it doesn't have a formula
class source_estuary(Variable):
    value_type = str
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Source Estuary of the oyster shipment"
    reference = "https://www.dpi.nsw.gov.au/fishing/commercial/fisheries/egf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class destination_estuary(Variable):
    value_type = str
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Destination Estuary of the oyster shipment"
    reference = "https://www.dpi.nsw.gov.au/fishing/commercial/fisheries/egf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class name(Variable):
    value_type = str
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Estuary name of the oyster shipment"
    reference = "https://www.dpi.nsw.gov.au/fishing/commercial/fisheries/egf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class source_estuary_status(Variable):
    value_type = str
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Status of the oyster shipment"
    reference = "Valid statuses are open/closed"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class destination_estuary_status(Variable):
    value_type = str
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Status of the oyster shipment"
    reference = "Valid statuses are open/closed"  # Always use the most official source

class EstuaryShipmentStatus(Enum):
    shipment_not_allowed = u'Oyster shipment from source to destination estuary not allowed'
    shipment_allowed = u'Oyster shipment from source to destination estuary allowed'

class estuary_movement(Variable):
    value_type = float
    # possible_values = EstuaryShipmentStatus
    # default_value = EstuaryShipmentStatus.shipment_not_allowed
    entity = Shipment
    definition_period = ETERNITY
    label = "The source and destination estuaries."

    def formula(shipment, period, _parameters):
        """An estuary movement."""
        #return_status = EstuaryShipmentStatus.shipment_allowed #open is 1
        if shipment("source_estuary", period) == \
           shipment("destination_estuary", period) :
            return_status = 1
        else:
            return_status = 0

        # logging.warning('Watch out!')
        if shipment("source_estuary_status", period) == "open" and \
           shipment("destination_estuary_status", period) == "open":
            return_status = 1
        else:
            return_status = 0
        #movements = estuary.members("movement", period)
        return return_status
