from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
	return self.name

#We're building a model for storing a ChatRoom. 
#Note that this specific tutorial doesn't go so far as to store actual chat messages to disk, 
#so we won't need a ChatMessage model (though that model is probably present in the sample code 
#provided at the end of this sequence). That's work for a future followup.