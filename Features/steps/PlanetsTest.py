from pytest_bdd import scenario, given, when, then
from behave import *


@when("I call method new_age with arguments equal 662256000 and Merkury")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Merkury")


@then("I should get recalculated age on that Merkury calc")
def step_impl(context):
    assert context.calculated_age == 87.13


@when("I call method new_age with arguments equal 662256000 and Ziemia")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Ziemia")


@then("I should get recalculated age on that Ziemia calc")
def step_impl(context):
    assert context.calculated_age == 20.99


@when("I call method new_age with arguments equal 662256000 and Wenus")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Wenus")


@then("I should get recalculated age on that Wenus calc")
def step_impl(context):
    assert context.calculated_age == 34.11


@when("I call method new_age with arguments equal 662256000 and Mars")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Mars")


@then("I should get recalculated age on that Mars calc")
def step_impl(context):
    assert context.calculated_age == 11.16


@when("I call method new_age with arguments equal 662256000 and Jowisz")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Jowisz")


@then("I should get recalculated age on that Jowisz calc")
def step_impl(context):
    assert context.calculated_age == 1.77


@when("I call method new_age with arguments equal 662256000 and Saturn")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Saturn")


@then("I should get recalculated age on that Saturn calc")
def step_impl(context):
    assert context.calculated_age == 0.71


@when("I call method new_age with arguments equal 662256000 and Uran")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Uran")


@then("I should get recalculated age on that Uran calc")
def step_impl(context):
    assert context.calculated_age == 0.25


@when("I call method new_age with arguments equal 662256000 and Neptun")
def step_impl(context):
    context.calculated_age = context.temp.new_age(662256000, "Neptun")


@then("I should get recalculated age on that Neptun calc")
def step_impl(context):
    assert context.calculated_age == 0.13