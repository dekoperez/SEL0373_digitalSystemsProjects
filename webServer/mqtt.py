import paho.mqtt.client as mqtt


# Mqtt Object
class Mqtt(object):

    """Mqtt class

    """

    # Attributes

    message = None

    # Method: Magic

    def __init__(self):
        """mqtt.__init__
        @Description:

        @Args:
            void

        @Returns:
            void
        """
        self.client = mqtt.Client()
        self.client.on_connect = Mqtt.on_connect
        self.client.on_message = Mqtt.on_message
        self.client.connect("192.168.1.111", 1883, 60)
        self.client.loop_start()

    # Method: Static

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        """mqtt.on_connect
        @Description:

        @Args:
            client:
            userdata:
            flags:
            rc:

        @Returns:
            void
        """

        print("Connected with result code " + str(rc))
        client.subscribe("home/hallSensor")
        client.subscribe("home/pirSensor")

    @staticmethod
    def on_message(client, userdata, msg):
        """mqtt.on_message
        @Description:

        @Args:
            client:
        userdata:
        msg:

        @Returns:
            void
        """

        Mqtt.message = msg.topic + " " + str(msg.payload)
        print Mqtt.message

    # Method: Class

    def printPayload(self):
        """Mqtt.printPayload
        @Description:

        @Args:
            void

        @Returns:
            Mqtt.message:
        """

        return Mqtt.message