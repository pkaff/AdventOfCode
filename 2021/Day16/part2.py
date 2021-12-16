from functools import reduce
myin = ''.join([format(int(hexchar, 16), '0>4b') for hexchar in open("input.txt", "r").read().replace('\n', '')])
def parse_packets(packetstr, n_packets):
    ix = 0
    values = []
    for n in range(n_packets):
        version = packetstr[ix:ix+3]
        ix += 3
        typeid = packetstr[ix:ix+3]
        ix += 3
        if int(typeid, 2) == 4:
            literal_value = ''
            while True:
                last_package = True if packetstr[ix] == '0' else False
                ix += 1
                literal_value += packetstr[ix:ix+4]
                ix += 4
                if last_package:
                    break
            values.append(int(literal_value, 2))
        else:
            length_id = packetstr[ix]
            ix += 1
            subpacket_values = []
            if length_id == '0':
                subpacket_len = int(packetstr[ix:ix+15], 2)
                ix += 15
                parsed_len = 0
                while parsed_len != subpacket_len:
                    tmp_subpacket_len, tmp_subpacket_values = parse_packets(packetstr[ix + parsed_len:ix+subpacket_len], 1)
                    parsed_len += tmp_subpacket_len
                    subpacket_values.extend(tmp_subpacket_values)
                ix += subpacket_len
            elif length_id == '1':
                num_sub_packets = int(packetstr[ix:ix+11], 2)
                ix += 11
                subpacket_len, subpacket_values = parse_packets(packetstr[ix:], num_sub_packets)
                ix += subpacket_len
            op = ''
            if int(typeid, 2) == 0:
                values.append(sum(subpacket_values))
            elif int(typeid, 2) == 1:
                values.append(reduce(lambda a, b: a * b, subpacket_values))
            elif int(typeid, 2) == 2:
                values.append(min(subpacket_values))
            elif int(typeid, 2) == 3:
                values.append(max(subpacket_values))
            elif int(typeid, 2) == 5:
                values.append(1 if subpacket_values[0] > subpacket_values[1] else 0)
            elif int(typeid, 2) == 6:
                values.append(1 if subpacket_values[0] < subpacket_values[1] else 0)
            elif int(typeid, 2) == 7:
                values.append(1 if subpacket_values[0] == subpacket_values[1] else 0)
    return ix, values
packet_len, packet_values = parse_packets(myin, 1)
print(packet_values[0])