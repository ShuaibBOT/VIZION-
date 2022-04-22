using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Positioning : MonoBehaviour
{
    int NumOfHand;
    string handType;
    string rightHand;
    string handClass;
    int positionX;
    int positionY;
    bool num1_type;
    bool num2_type;

    // Start is called before the first frame update
    void Start()
    {
        // Checking whether the user is using only one hand and that hand is the left hand.
        if (NumOfHand == 1 && handType == "Left")
        {
            num1_type = true;
        }
        else
        {
            num1_type = false;
        }

        // Checking whether the user is using two hands
        if(NumOfHand == 2)
        {
            num2_type = true;
        }
        else
        {
            num2_type = false;
        }
          
    }

    // Update is called once per frame
    void Update()
    {
        if (num1_type == true)
        {
            if (handClass == "Grab") //Positioning
            {
                //if arm moves to the right (x val dec)
                for (int i = positionX; i < 650; i = positionX - 10)
                {
                    transform.position = Vector3.right;
                }

                //if arm moves to the left (x val inc)
                for (int i = positionX; i < 650; i = positionX + 10)
                {
                    transform.position += Vector3.left;
                }

                //if arm moves to the up (y val dec)
                for (int i = positionY; i < 480; i = positionY - 10)
                {
                    transform.position += Vector3.up;
                }

                //if arm moves to the down (y val inc)
                for (int i = positionY; i < 480; i = positionY + 10)
                {
                    transform.position += Vector3.down;
                }

            }
            else if (handClass == "Rotate") //Rotation
            {
                //if hand moves right (x val dec) (XYZ INC)
                for (int i = positionX; i < 650; i = positionX - 10)
                {
                    transform.Rotate(1, 1, 1);
                }
                //if hand moves up (y val inc) (XYZ INC)
                
                for (int i = positionY; i < 650; i = positionY + 10)
                {
                    transform.Rotate(1, 1, 1);
                }

                //if hand moves left (x val inc) (XYZ DEC)
                for (int i = positionX; i < 650; i = positionX + 10)
                {
                    transform.Rotate(-1, -1, -1);
                }

                //if hand moves down (y val dec) (XYZ DEC)
                for (int i = positionY; i < 650; i = positionY - 10)
                {
                    transform.Rotate(-1, -1, -1);
                }
            }
            else
            {
                return;
            }

        }
        else
        {
            return;
        }

        if(num2_type == true)
        {
            // if arm moves right (x val dec) or up (y val inc) obj moves on the axis speified by the user. INCREASE the value.
            // if arm moves left (x val inc) or down (y val dec) obj moves on the axis speified by the user. DECREASE the value.
            if (handType == "Left" && handClass == "Grab" && rightHand == "X axis")
            {
                for (int i = positionX; i < 650; i = positionX - 10) // X axis inc by 1
                {
                    transform.position += Vector3.right;
                }
                for (int i = positionY; i < 480; i = positionY + 10)  // X axis inc by 1
                {
                    transform.position += Vector3.right;
                }

                for (int i = positionX; i < 650; i = positionX + 10)  // X axis dec by 1
                {
                    transform.position += Vector3.left;
                }
                for (int i = positionY; i < 480; i = positionY - 10)  // X axis dec by 1
                {
                    transform.position += Vector3.left;
                }
            }
            else if(handType == "Left" && handClass == "Grab" && rightHand == "Y axis")
            {
                for (int i = positionX; i < 650; i = positionX - 10)  // Y axis inc by 1
                {
                    transform.position += Vector3.up;
                }
                for (int i = positionY; i < 480; i = positionY + 10) // Y axis inc by 1
                {
                    transform.position += Vector3.up;
                }

                for (int i = positionX; i < 650; i = positionX + 10) // Y axis dec by 1
                {
                    transform.position += Vector3.down;
                }
                for (int i = positionY; i < 480; i = positionY - 10) // Y axis dec by 1
                {
                    transform.position += Vector3.down;
                }
            }
            else if(handType == "Left" && handClass == "Grab" && rightHand == "Z axis")
            {
                for (int i = positionX; i < 650; i = positionX - 10) // Z axis inc by 1
                {
                    transform.position += Vector3.forward;
                }
                for (int i = positionY; i < 480; i = positionY + 10) // Z axis inc by 1
                {
                    transform.position += Vector3.forward;
                }

                for (int i = positionX; i < 650; i = positionX + 10) // Z axis dec by 1
                {
                    transform.position += Vector3.back;
                }
                for (int i = positionY; i < 480; i = positionY - 10) // Z axis dec by 1
                {
                     transform.position += Vector3.back;
                }
            }
            else
            {
                return;
            }

            //if hand moves Right(x value decreases)or UP(y value increases): object rotates based on the axis specified by the user.(increases rotation value)
            //if hand moves left(x value increases) or DOwn(y value decrease): object rotates based on the axis specified by the user. (decreases rotation value)
            if (handType == "Left" && handClass == "Rotate" && rightHand == "X axis") 
            {
                for (int i = positionX; i < 650; i = positionX - 10) // X axis inc by 1
                {
                    transform.Rotate(Vector3.right);
                }
                for (int i = positionY; i < 480; i = positionY + 10)  // X axis inc by 1
                {
                    transform.Rotate(Vector3.right);
                }
                for (int i = positionX; i < 650; i = positionX + 10)  // X axis dec by 1
                {
                    transform.Rotate(Vector3.left);
                }
                for (int i = positionY; i < 480; i = positionY - 10)  // X axis dec by 1
                {
                    transform.Rotate(Vector3.left);
                }
            }
            else if (handType == "Left" && handClass == "Rotate" && rightHand == "Y axis")
            {
                for (int i = positionX; i < 650; i = positionX - 10)  // Y axis inc by 1
                {
                    transform.Rotate(Vector3.up);
                }
                for (int i = positionY; i < 480; i = positionY + 10) // Y axis inc by 1
                {
                    transform.Rotate(Vector3.up);
                }
                for (int i = positionX; i < 650; i = positionX + 10) // Y axis dec by 1
                {
                    transform.Rotate(Vector3.down);
                }
                for (int i = positionY; i < 480; i = positionY - 10) // Y axis dec by 1
                {
                    transform.Rotate(Vector3.down);
                }
            }
            else if (handType == "Left" && handClass == "Rotate" && rightHand == "Z axis")
            {
                for (int i = positionX; i < 650; i = positionX - 10) // Z axis inc by 1
                {
                    transform.Rotate(Vector3.forward);
                }
                for (int i = positionY; i < 480; i = positionY + 10) // Z axis inc by 1
                {
                    transform.Rotate(Vector3.forward);
                }
                for (int i = positionX; i < 650; i = positionX + 10) // Z axis dec by 1
                {
                    transform.Rotate(Vector3.back);
                }
                for (int i = positionY; i < 480; i = positionY - 10) // Z axis dec by 1
                {
                    transform.Rotate(Vector3.back);
                }
            }
            else
            {
                return;
            }
        }
        else
        {
            return;
        }

    }
}
