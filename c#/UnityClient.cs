using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using System.Threading;
using System;

public class UnityClient : MonoBehaviour
{
    private string TAG = "UnityClient: ";

    Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    Vector3 receivedPos = Vector3.zero;

    bool running;
    bool moving;


    GameObject balloon;

    Vector3 target;
    Vector3 pos;
    Vector3 startPosition;
    float weight = 0.0f;
    float liftSpeed = 1.2f;
    float prev_biofeedback = -1000f;
    

    private void Update()
    {
        // transform.position = receivedPos;
        float biofeedback = receivedPos.x;



        if (biofeedback != prev_biofeedback)
        {
            Debug.Log("Biofeedback: " + biofeedback.ToString());
            target = balloon.transform.position;
            startPosition = target;
            pos = new Vector3(target.x, biofeedback, target.z);
            target = pos;
            //target.y *= biofeedback;
            if(target.y >= 1f)
            {
                prev_biofeedback = biofeedback;
                moving = true;
            }

        }

        if(moving == true && balloon.transform.position == target)
        {
            moving = false;
            weight = 0.0f;
        }

        if (moving)
        {
            weight += Time.deltaTime * liftSpeed;
            balloon.transform.position = Vector3.Lerp(startPosition,
                                              target, weight);
        }
    }

    private void Start()
    {

        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();
        balloon = GameObject.Find("OVRCameraRig");
        //balloon.transform.position = new Vector3(0f, 10.0f, 0f);

    }

    void GetInfo()
    {
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();

        client = listener.AcceptTcpClient();

        running = true;
        while (running)
        {
            SendAndReceiveData();
        }
        listener.Stop();
    }

    void SendAndReceiveData()
    {
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];

        //---receiving Data from the Host----
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string
       
        if (dataReceived != null)
        {
            //---Using received data---
            receivedPos = StringToVector3(dataReceived); //<-- assigning receivedPos value from Python
            //---Sending Data to Host----
            byte[] myWriteBuffer = Encoding.ASCII.GetBytes("Received in Unity"); //Converting string to byte data
            nwStream.Write(myWriteBuffer, 0, myWriteBuffer.Length); //Sending the data in Bytes to Python 
        }
    }

    public static Vector3 StringToVector3(string sVector)
    {
        // Remove the parentheses
        if (sVector.StartsWith("(") && sVector.EndsWith(")"))
        {
            sVector = sVector.Substring(1, sVector.Length - 2);
            
        }

        // split the items
        string[] sArray = sVector.Split(',');

        // store as a Vector3
        Vector3 result = new Vector3(
            //float.Parse(sArray[0].Replace('.',',')),
            float.Parse(sArray[0]),
            float.Parse(sArray[1]),
            float.Parse(sArray[2]));

        Debug.Log("UnityClient: " + result.ToString());
        return result;
    }
}