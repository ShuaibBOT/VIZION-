using System;
using System.Runtime.InteropServices;
using UnityEngine;

public class myNativeScript : MonoBehaviour
{
    const string dll = "nativeUnityPlugin5";

    [DllImport(dll)]
    private static extern void SeedRandomizer();

    [DllImport(dll)]
    private static extern int DieRoll(int sides);

    [DllImport(dll)]
    private static extern float Add(float a, float b);

    [DllImport(dll)]
    private static extern float Random();

    [DllImport(dll)]
    private static extern IntPtr HelloWorld();

    // Start is called before the first frame update
    void Start()
    {
        SeedRandomizer();

        Debug.Log(Add(3.2f, 4.5f).ToString());
        Debug.Log(DieRoll(20).ToString());
        Debug.Log(Random().ToString());
        Debug.Log(Marshal.PtrToStringAnsi(HelloWorld()));
    }
}