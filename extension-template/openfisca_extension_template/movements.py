"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
from openfisca_core.tracers import ComputationLog
from openfisca_core.periods import MONTH, ETERNITY
from openfisca_core.variables import Variable
from openfisca_core.indexed_enums import Enum

# Import the Entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import Shipment
#logger = ComputationLog(full_tracer)

# This variable is a pure input: it doesn't have a formula
class source_estuary(Variable):
    value_type = str
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Source Estuary of the oyster shipment"
    reference = "https://www.dpi.nsw.gov.au/fishing/commercial/fisheries/egf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class source_status(Variable):
    value_type = float
    entity = Shipment
    definition_period = ETERNITY
    #set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Source status of the oyster shipment"
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

class is_source_estuary_closed(Variable):
    value_type = bool
    entity = Shipment
    definition_period = ETERNITY
    label = "Source estuary closed"

    def formula(shipments, period, parameters):
        source_estuary_status = shipments("source_estuary_status", period)
        condition_is_estuary_closed = (source_estuary_status == EstuaryShipmentStatus.closed)
        return where(condition_is_estuary_closed, 1, 0)

class EstuaryShipmentStatus(Enum):
    closed = u'Source estuary closed'
    is_same_estuary_movement = u'Same estuary movement'

class estuary_movement_multiple(Variable):
    value_type = str
    # possible_values = EstuaryShipmentStatus
    # default_value = EstuaryShipmentStatus.shipment_not_allowed
    entity = Shipment
    definition_period = ETERNITY
    label = "The source and destination estuaries."

    def formula(shipments, period, parameters):
        """An estuary movement."""

        source_estuary_status = shipments("source_estuary_status", period)
        print(source_estuary_status)
        #logger.print_log()
        #return_status = EstuaryShipmentStatus.shipment_allowed #open is 1
        # if shipments("source_estuary", period) == \
        #    shipments("destination_estuary", period) :
        #     estuary_same = 1
        # else:
        #     estuary_same = 0

        # logging.warning('Watch out!')

        # result_str = "Source estuary closed. Movement not permitted"
        #result_str = shipments("source_estuary_status", period) == "closed"

        result_str = shipments("source_estuary", period) == shipments("destination_estuary", period)
        is_source_estuary_closed = (source_estuary_status == EstuaryShipmentStatus.closed)

        #result_str = shipments("source_estuary_status", period) == "closed"

        #condition_shipment = shipments('source_status', period) == 1

        #movements = estuary.members("movement", period)
        #return (estuary_same + movement_permitted)
        # result_str = "closed"
        #return where(result_str, "Source estuary closed. Movement not permitted", "Movement permitted")
        #return where(result_str,"Movement permitted", "Movement not permitted" )
        return select([is_source_estuary_closed],
            ['closed'])


class estuary_movement(Variable):
    value_type = str
    # possible_values = EstuaryShipmentStatus
    # default_value = EstuaryShipmentStatus.shipment_not_allowed
    entity = Shipment
    definition_period = ETERNITY
    label = "The source and destination estuaries."

    def formula(shipments, period, parameters):
        """An estuary movement."""
        result_str = shipments("source_estuary_status", period) == "closed"

        #condition_shipment = shipments('source_status', period) == 1

        #movements = estuary.members("movement", period)
        #return (estuary_same + movement_permitted)
        # result_str = "closed"
        #return where(result_str, "Source estuary closed. Movement not permitted", "Movement permitted")
        return where(result_str,"Movement not permitted", "Movement permitted" )
