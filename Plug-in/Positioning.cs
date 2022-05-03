using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Positioning : MonoBehaviour
{
    public UDPReceive udpReceive;
    private GameObject handPoints;
    string handType;
    string handType2;
    public string LHFingers;
    public string RHFingers;
    public string RHFingers2;
    string handClass;

    // Start is called before the first frame update
    void Start()
    {
        handPoints = GameObject.Find("Test");
    }

    // Update is called once per frame
    void Update()
    {
        string centerPoints = udpReceive.centerPoints;
        centerPoints = centerPoints.Remove(0, 1);
        centerPoints = centerPoints.Remove(centerPoints.Length - 1, 1);


        string[] points = centerPoints.Split(',');

        if (points.Length == 6)
        {
            RHFingers = points[0] + points[1] + points[2] + points[3] + points[4];
            print("Right :" + RHFingers);

            if (RHFingers == "1 1 1 1 1")
            {
                Vector3 temp = new Vector3(0.01f, 0, 0); //positioning x axis
                handPoints.transform.position += temp;
                print("Positioning");
            }
            else if (RHFingers == "0 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.1f, 0, 0); //rotate x axis
                handPoints.transform.Rotate(temp);
                print("Rotation");
            }
            else if (RHFingers == "1 1 0 0 0")
            {
                Vector3 temp = new Vector3(0.01f, 0.01f, 0.01f); //scaling x axis
                handPoints.transform.localScale += temp;
                print("Scale");
            }
            else
            {
                print("Not Recognized");
            }
        }

        if (points.Length == 13)
        {
            handType = points[0];
            if (handType == "Left")
            {
                LHFingers = points[1] + points[2] + points[3] + points[4] + points[5];
                RHFingers2 = points[7] + points[8] + points[9] + points[10] + points[11];
            }
            else
            {
                LHFingers = points[7] + points[8] + points[9] + points[10] + points[11];
                RHFingers2 = points[1] + points[2] + points[3] + points[4] + points[5];
            }


            print("Right : " + RHFingers2);
            print("Left : " + LHFingers);


            if (RHFingers2 == " 1 1 1 1 1" && LHFingers == " 1 0 0 0 1")
            {
                Vector3 temp = new Vector3(0, 0, 0.01f); //grab z axis
                handPoints.transform.position += temp;
                print("Positioning Z axis");
            }

            else if (RHFingers2 == " 1 1 1 1 1" && LHFingers == " 0 1 1 0 0")
            {
                Vector3 temp = new Vector3(0, 0.01f, 0); //grab y axis
                handPoints.transform.position += temp;
                print("Positioning Y axis");
            }

            else if (RHFingers2 == " 1 1 1 1 1" && LHFingers == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.01f, 0, 0); //grab x axis
                handPoints.transform.position += temp;
                print("Positioning X axis");
            }

            else if (RHFingers2 == " 0 0 0 0 0" && LHFingers == " 1 0 0 0 1")
            {
                Vector3 temp = new Vector3(0, 0, 0.1f); //rotate z axis
                handPoints.transform.Rotate(temp);
                print("Rotation Z axis");
            }

            else if (RHFingers2 == " 0 0 0 0 0" && LHFingers == " 0 1 1 0 0")
            {
                Vector3 temp = new Vector3(0, 0.1f, 0); //rotate y axis
                handPoints.transform.Rotate(temp);
                print("Rotation Y axis");
            }

            else if (RHFingers2 == " 0 0 0 0 0" && LHFingers == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.1f, 0, 0); //rotate x axis
                handPoints.transform.Rotate(temp);
                print("Rotation X axis");
            }

            else if (RHFingers2 == " 1 1 0 0 0" && LHFingers == " 1 0 0 0 1")
            {
                Vector3 temp = new Vector3(0, 0, 0.01f); //scaling z axis
                handPoints.transform.localScale += temp;
                print("Scale Z axis");
            }

            else if (RHFingers2 == " 1 1 0 0 0" && LHFingers == " 0 1 1 0 0")
            {
                Vector3 temp = new Vector3(0, 0.01f, 0); //scaling y axis
                handPoints.transform.localScale += temp;
                print("Scale Y axis");
            }

            else if (RHFingers2 == " 1 1 0 0 0" && LHFingers == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.01f, 0, 0); //scaling x axis
                handPoints.transform.localScale += temp;
                print("Scale X axis");
            }
            else
            {
                print("Not Recognized");
            }

        }
    }
}