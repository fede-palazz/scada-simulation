import assets.helloworld_pb2 as HelloWorld

hello = HelloWorld.HelloMessage()
hello.name = "World"

print(hello)

hello_ser = hello.SerializeToString()
print(hello_ser)

newHello = HelloWorld.HelloMessage()
newHello.ParseFromString(hello_ser)
print(newHello.name)
