class Constants(object):
    def __init__(self):
        self.vocabulary_size = 8000
        self.hidden_layer_size = 100
        self.training_size = 100000
        self.unknown_token = "UNKNOWN_TOKEN"
        self.sentence_start_token = "SENTENCE_START"
        self.sentence_end_token = "SENTENCE_END"
        self.datapath = 'songlyrics/songdata.csv'
        self.num_sentences = 10
        self.mode_lstm = 'lstm'
        self.mode_rnn = 'simple_rnn'
        self.sentence_min_length = 7
        self.lstm_seq_length = 100