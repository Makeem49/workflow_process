from rest_framework import generics

# Create your views here.
class ActionCreateView(generics.CreateAPIView):
    """View to create a customise action to be taken by a user who have access to the step"""


class ActionDetailView(generics.CreateAPIView):
    """View to perform the action to be taken by a user who have access to the step"""


class ActionUpdateView(generics.RetrieveUpdateAPIView):
    """View to update a user action for a particular step"""


class ActionDeleteView(generics.RetrieveDestroyAPIView):
    """View to detele a particular action taken by the user."""



