import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

Future<PersonList> fetchAlbum() async {
  final response = await http.get(
    Uri.parse('http://127.0.0.1:5000/'),
  );
  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return PersonList.fromJson(jsonDecode(response.body));
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

class Person {
  final String name;
  final bool present;

  Person({
    required this.name,
    required this.present,
  });

  factory Person.fromJson(Map<String, dynamic> json) {
    return Person(
      name: json['name'],
      present: json['present'],
    );
  }
}

class PersonList {
  final List<Person> people;

  PersonList({
    this.people = const [],
  });
  factory PersonList.fromJson(List<dynamic> parsedJson) {
    List<Person> people = [];
    people = parsedJson.map((i) => Person.fromJson(i)).toList();

    // ignore: unnecessary_new
    return new PersonList(
      people: people,
    );
  }
}

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late Future<PersonList> futureAlbum;
  String dstring = "";

  @override
  void initState() {
    super.initState();
    new Timer.periodic(Duration(seconds: 30), (Timer t) => setState(() {}));
    futureAlbum = fetchAlbum();
  }


  @override
  Widget build(BuildContext context) {
    Future<PersonList> futureAlbum = fetchAlbum();
    return MaterialApp(
      title: 'Whos Home?',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Whos Home?'),
        ),
        body: Column(
          children: [
            Expanded(
            child:FutureBuilder<PersonList>(
            future: futureAlbum,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                if (snapshot.data!.people[0].present) {
                  print("d");
                  dstring = "David is Home!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.green));
                } else {
                  print("nd");
                  dstring = "David is Away!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.red));
                }
                
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),),
          Expanded(child: FutureBuilder<PersonList>(
            future: futureAlbum,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                if (snapshot.data!.people[1].present) {
                  print("n");
                  dstring = "Nathan is Home!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.green));;
                } else {
                  print("nn");
                  dstring = "Nathan is Away!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.red));;
                }
                
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
          ),
           Expanded(child: FutureBuilder<PersonList>(
            future: futureAlbum,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                if (snapshot.data!.people[3].present) {
                  print("k");
                  dstring = "Kajetan is Home!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.green));;
                } else {
                  print("nk");
                  dstring = "Kajetan is Away!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.red));;
                }
                
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
          ),
           Expanded(child: FutureBuilder<PersonList>(
            future: futureAlbum,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                if (snapshot.data!.people[2].present) {
                  print("c");
                  dstring = "Clement is Home!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.green));;
                } else {
                  print("nc");
                  dstring = "Clement is Away!";
                  return Text(dstring, style: TextStyle(fontSize: 20, color: Colors.red));;
                }
                
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
          )
          ]
      ),
      )
    );
  }
  
}

@override
Widget build(BuildContext context) {
  // TODO: implement build
  throw UnimplementedError();
}
