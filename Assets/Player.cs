using System;
using System.IO;
using System.Net.Sockets;
using UnityEngine;

public class Player : MonoBehaviour
{
    TcpClient client;
    NetworkStream stream;
    BinaryReader reader;

    void Start()
    {
        client = new TcpClient("localhost", 12345);
        stream = client.GetStream();
        reader = new BinaryReader(stream);
    }

    void Update()
    {
        if (stream.DataAvailable)
        {
            int x = reader.ReadInt32();
            int y = reader.ReadInt32();

            y = -y;

            Vector3 newPos = new Vector3(x, y, 0) * 0.01f;
            transform.position = newPos;
        }
    }

    void OnApplicationQuit()
    {
        reader.Close();
        stream.Close();
        client.Close();
    }
}
