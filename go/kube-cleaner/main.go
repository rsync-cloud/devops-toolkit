package main

import (
    "context"
    "flag"
    "fmt"
    "os"
    "path/filepath"

    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
    "k8s.io/client-go/util/homedir"
)

func main() {
    var namespace string
    flag.StringVar(&namespace, "namespace", "default", "Namespace to clean")
    flag.Parse()

    kubeconfig := filepath.Join(homedir.HomeDir(), ".kube", "config")
    config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
    if err != nil {
        fmt.Printf("Error building kubeconfig: %v\n", err)
        os.Exit(1)
    }

    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        fmt.Printf("Error creating Kubernetes client: %v\n", err)
        os.Exit(1)
    }

    pods, err := clientset.CoreV1().Pods(namespace).List(context.Background(), metav1.ListOptions{FieldSelector: "status.phase=Failed"})
    if err != nil {
        fmt.Printf("Error listing pods: %v\n", err)
        os.Exit(1)
    }

    for _, pod := range pods.Items {
        fmt.Printf("Deleting failed pod: %s\n", pod.Name)
        err := clientset.CoreV1().Pods(namespace).Delete(context.Background(), pod.Name, metav1.DeleteOptions{})
        if err != nil {
            fmt.Printf("Error deleting pod %s: %v\n", pod.Name, err)
        }
    }
}
