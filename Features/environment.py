from planets import Planets


def before_scenario(context, scenario):
    if 'planets_setup' in scenario.feature.tags:
        print('rrun')
        context.temp = Planets()


def after_scenario(context, scenario):
    pass

# @when("I call method new_age with arguments equal (?P<age>.+) and (?P<planet>.+)")
# def step_impl(context, age, planet):
#     context.calculated_age = context.temp.new_age(age, planet)
#
# @then("I should get recalculated age on that planet (?P<calculated>.+)")
# def step_impl(context, calculated):
#     context.calculated_age = calculated
