# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django import forms

from djanban.apps.base.auth import get_member_boards
from djanban.apps.boards.models import Label
from djanban.apps.recurrent_cards.models import WeeklyRecurrentCard


# Work hours package filter
class RecurrentCardFilterForm(forms.Form):

    label = forms.ChoiceField(label="Label", choices=[], required=False)
    is_active = forms.ChoiceField(label="Active?", choices=[], required=False)

    def __init__(self, *args, **kwargs):
        self.member = kwargs.pop("member")
        self.board = kwargs.pop("board")
        super(RecurrentCardFilterForm, self).__init__(*args, **kwargs)

        # Available labels for this user
        self.fields["label"].choices = [("", "None")] + [
            (label.id, label.name) for label in self.board.labels.exclude(name="").order_by("name")]

        # Is paid?
        self.fields["is_active"].choices = [("", "Indiferent"),("Yes", "Yes"),("No", "No")]

    def clean(self):
        return super(RecurrentCardFilterForm, self).clean()

    def get_recurrent_cards(self):
        # Filtering by board or label
        label_id = self.cleaned_data.get("label")
        recurrent_cards = self.member.recurrent_cards.filter(board=self.board).order_by("name")
        if label_id:
            label = self.boards.labels.get(id)
            recurrent_cards = recurrent_cards.filter(labels=label)

        # Filtering paid work hours packages
        if self.cleaned_data.get("is_active") in ["Yes", "No"]:
            recurrent_cards = recurrent_cards.filter(is_paid=(self.cleaned_data.get("is_active") == "Yes"))

        return recurrent_cards


class WeeklyRecurrentCardForm(forms.ModelForm):
    class Meta:
        model = WeeklyRecurrentCard
        fields = [
            "name", "description", "position", "estimated_time", "creation_list",
            "labels", "members",
            "create_on_mondays", "create_on_tuesdays", "create_on_wednesdays", "create_on_thursdays",
            "create_on_fridays", "create_on_saturdays", "create_on_sundays", "move_to_list_when_day_ends",
            "is_active"
        ]

    class Media:
        css = {
            'all': ('css/recurrent_cards/form.css',)
        }
        js = (
            'js/recurrent_cards/form.js',
        )

    def __init__(self, *args, **kwargs):
        self.member = kwargs.pop("member")
        self.board = kwargs.pop("board")
        super(WeeklyRecurrentCardForm, self).__init__(*args, **kwargs)

        # Lists of this board
        active_lists = [(list_.id, list_.name) for list_ in self.board.active_lists.order_by("position")]
        self.fields["creation_list"].choices = active_lists
        self.fields["move_to_list_when_day_ends"].choices = [("", "Don't move")] + active_lists

        # Member team mates of this user
        self.fields["members"].choices = \
            [(member.id, member.external_username) for member in self.board.members.all()]

        # Available labels for this board
        self.fields["labels"].choices = \
            [(label.id, label.name) for label in self.board.labels.exclude(name="").order_by("name")]

    def save(self, commit=True):
        super(WeeklyRecurrentCardForm, self).save(commit)
        if (
            commit
            and not self.instance.members.filter(
                id=self.instance.creator.id
            ).exists()
        ):
            self.instance.members.add(self.instance.creator)


# Delete recurrent card
class DeleteWeeklyRecurrentCardForm(forms.Form):
    confirmed = forms.BooleanField(label=u"Confirm you want to delete this recurrent card")