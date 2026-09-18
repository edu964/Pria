import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class Desafio(Node):

    def __init__(self):
        super().__init__('nododesafio1')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.subscription = self.create_subscription(
            LaserScan,
            '/base_scan',
            self.leer_laser,
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        self.contador = 0
        self.distancia_frente = 10.0


    def leer_laser(self, msg):

        centro = len(msg.ranges) // 2
        self.distancia_frente = msg.ranges[centro]


    def timer_callback(self):

        msg = Twist()

        print("Distancia frontal:", self.distancia_frente)


        # 0 A 14
        # GIRA 15 VECES A LA IZQUIERDA
        if self.contador < 15:

            msg.linear.x = 0.0
            msg.angular.z = 0.5

            self.contador += 1


        # CONTADOR = 15
        # AVANZA HASTA DISTANCIA MENOR A 2.4
        elif self.contador == 15:

            if self.distancia_frente >= 2.8:

                msg.linear.x = 0.8
                msg.angular.z = 0.0

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.contador += 1


        # 16 A 45
        # GIRA 30 VECES A LA DERECHA
        elif self.contador <= 45:

            msg.linear.x = 0.0
            msg.angular.z = -0.5

            self.contador += 1


        # CONTADOR = 46
        # AVANZA HASTA DISTANCIA MENOR A 1.2
        elif self.contador == 46:

            if self.distancia_frente >= 1.2:

                msg.linear.x = 0.8
                msg.angular.z = 0.0

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.contador += 1


        # 47 A 76
        # GIRA 30 VECES A LA IZQUIERDA
        elif self.contador <= 76:

            msg.linear.x = 0.0
            msg.angular.z = 0.5

            self.contador += 1


        # CONTADOR = 77
        # AVANZA HASTA DISTANCIA MENOR A 1.0
        elif self.contador == 77:

            if self.distancia_frente >= 1.0:

                msg.linear.x = 0.8
                msg.angular.z = 0.0

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.contador += 1


        # 78 A 107
        # GIRA 30 VECES A LA DERECHA
        elif self.contador <= 107:

            msg.linear.x = 0.0
            msg.angular.z = -0.5

            self.contador += 1


        # CONTADOR = 108
        # AVANZA HASTA DISTANCIA MENOR A 2.8
        elif self.contador == 108:

            if self.distancia_frente >= 2.8:

                msg.linear.x = 0.8
                msg.angular.z = 0.0

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.contador += 1


        # 109 A 140
        # GIRA 32 VECES A LA DERECHA
        elif self.contador <= 140:

            msg.linear.x = 0.0
            msg.angular.z = -0.5

            self.contador += 1


        # CONTADOR = 141
        # AVANZA HASTA DISTANCIA MENOR A 1.3
        elif self.contador == 141:

            if self.distancia_frente >= 0.2:

                msg.linear.x = 0.8
                msg.angular.z = 0.0

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.contador += 1


        # TERMINA
        else:

            msg.linear.x = 0.0
            msg.angular.z = 0.0


        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = Desafio()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
