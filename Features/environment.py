from planets import Planets
from pangram import Pangram


def before_scenario(context, scenario):
    if 'planets_setup' in scenario.feature.tags:
        context.temp = Planets()

def after_scenario(context, scenario):
    if 'planets_setup' in scenario.feature.tags:
        context.temp = None
