class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for str in strs:
            encoded_str = f"{len(str)}#{str}"
            encoded_list.append(encoded_str)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            delimiter_index = s.find("#", i)
            number = s[i:delimiter_index]
            decoded_list.append(s[(delimiter_index + 1):(delimiter_index + int(number)) + 1])
            i = delimiter_index + int(number) + 1
        return decoded_list