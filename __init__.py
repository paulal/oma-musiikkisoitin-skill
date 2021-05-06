import os

from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG # for logging outside of the class
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel


class OmaMusiikkisoitin(CommonPlaySkill):

    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.

            The method is invoked by the PlayBackControlSkill.

            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        library = open('/home/pomo/.config/cmus/lib.pl')
        my_songs = []
        for line in library:
            mySongs.append(line.strip())
        library.close()

        self.log.info(my_songs)
        
        # Get match and confidence
        match, confidence = match_one(phrase, my_songs)
        # If the confidence is high enough return a match
        if confidence > 0.5:
            return (match, CPSMatchLevel.TITLE, {"track": match})
        # Otherwise return None
        else:
            return None
        
    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        # Retrieve the track url from the data
        url = data['track']
        self.audioservice.play(url)  # Send url to audioservice to start playback

    @intent_file_handler('play.something.intent')
    def handle_play_something(self, message):
        self.log.info('handle_play_something activated')
        self.speak_dialog('play.something')
        


def create_skill():
    return OmaMusiikkisoitin()

