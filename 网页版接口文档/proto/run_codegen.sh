#!/bin/bash

rm -f *_pb2.py *_pb2.pyc

# Runs the protoc with gRPC plugin to generate protocol messages and gRPC stubs.
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./header.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./connect.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./base.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./house.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./user.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./booking.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./homepage.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./house_calendar.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./comment.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./chat.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./draw_money.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./id_alloc.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./search.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./statistics.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./count.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./coupon.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./statement.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./sms_router.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./ota.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./const.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./merchant.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./lucky_card.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./seq_alloc.proto
protoc -I ./ --cpp_out=../../conn ./transfer_server.proto
protoc -I ./ --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ./seq_alloc_dispatcher.proto

