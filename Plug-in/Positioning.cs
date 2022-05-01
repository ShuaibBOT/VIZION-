using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Positioning : MonoBehaviour
{
    public UDPReceive udpReceive;
    private GameObject handPoints;
    int NumOfHand;
    public string handType; 
    string handType2;
    public int positionXL;
    public int positionYL;
    public string LHFingers;
    string RHFingers;
    string LHFingers2;
    int positionXR;
    int positionYR;
    string handClass;
    //bool num1_type = false;
    int LHX;
    int LHY;
    //bool num2_type = false;

    // Start is called before the first frame update
    void Start()
    {
        handPoints = GameObject.Find("Test");
    }

    // Update is called once per frame
    void Update()
    {
        string centerPoints = udpReceive.centerPoints;
        centerPoints = centerPoints.Remove(0,1);
        centerPoints = centerPoints.Remove(centerPoints.Length-1,1);
        print(centerPoints);

        string[] points = centerPoints.Split(',');
        //positionX = int.Parse(points[0]); 
        //positionY = int.Parse(points[1]);
        //print(positionX); //xvalue of LH
        //print(positionY); //y value of LH
        
        if (points.Length == 8)
        {
            handType = points[7].ToString();
            print(handType);

            LHFingers = points[2] + points[3] + points[4] + points[5] + points[6];
            print(LHFingers);

            positionXL = int.Parse(points[0]);
            positionYL = int.Parse(points[1]);

            LHX = positionXL; print(LHX);
            LHY = positionYL; print(LHY);

            if (LHFingers == " 0 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.01f, 0, 0);
                handPoints.transform.position += temp;
                print("Positioning");
            }
            else if(LHFingers == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.1f, 0, 0); //rotate x axis
                handPoints.transform.Rotate(temp);
                print("Rotation");
            }
            else if(LHFingers == " 1 1 0 0 0")
            {
                Vector3 temp = new Vector3(0.01f, 0, 0); //scaling x axis
                handPoints.transform.localScale += temp;
                print("Scale");
            }
            else
            {
                print("Not Recognized");
            }
        }
  
        if (points.Length == 16)
        {
            handType2 = points[14].ToString();
            print(handType2);

            RHFingers = points[4] + points[5] + points[6] + points[7] + points[8];
            LHFingers2 = points[9] + points[10] + points[11] + points[12] + points[13];
            print(RHFingers);

            positionXR = int.Parse(points[0]); print(positionXR);
            positionYR = int.Parse(points[1]); print(positionYR);

            if (RHFingers == " 1 0 1 1 1" && LHFingers2 == " 0 0 0 0 0")
            {
                Vector3 temp = new Vector3(0, 0, 0.01f); //grab z axis
                handPoints.transform.position += temp;
                print("Positioning Z axis");
            }

            else if (RHFingers == " 0 1 1 0 0" && LHFingers2 == " 0 0 0 0 0")
            {
                Vector3 temp = new Vector3(0, 0.01f, 0); //grab y axis
                handPoints.transform.position += temp;
                print("Positioning Y axis");
            }

            else if (RHFingers == " 1 0 0 0 1" && LHFingers2 == " 0 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.01f, 0, 0); //grab x axis
                handPoints.transform.position += temp;
                print("Positioning X axis");
            }

            else if (RHFingers == " 1 0 1 1 1" && LHFingers2 == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0, 0, 0.1f); //rotate z axis
                handPoints.transform.Rotate(temp);
                print("Rotation Z axis");
            }

            else if (RHFingers == " 0 1 1 0 0" && LHFingers2 == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0, 0.1f, 0); //rotate y axis
                handPoints.transform.Rotate(temp);
                print("Rotation Y axis");
            }

            else if (RHFingers == " 1 0 0 0 1" && LHFingers2 == " 1 0 0 0 0")
            {
                Vector3 temp = new Vector3(0.1f, 0, 0); //rotate x axis
                handPoints.transform.Rotate(temp);
                print("Rotation X axis");
            }

            else if (RHFingers == " 1 0 1 1 1" && LHFingers2 == " 1 1 0 0 0")
            {
                Vector3 temp = new Vector3(0, 0, 0.01f); //scaling z axis
                handPoints.transform.localScale += temp;
                print("Scale Z axis");
            }

            else if (RHFingers == " 0 1 1 0 0" && LHFingers2 == " 1 1 0 0 0")
            {
                Vector3 temp = new Vector3(0, 0.01f, 0); //scaling y axis
                handPoints.transform.localScale += temp;
                print("Scale Y axis");
            }

            else if (RHFingers == " 1 0 0 0 1" && LHFingers2 == " 1 1 0 0 0")
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
