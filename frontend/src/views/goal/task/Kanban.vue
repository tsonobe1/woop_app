<template>
  <div>
    <div id="css-grid">
      <!-- 難しさと満足度はVuetifyのRatingを使うとよいかも　https://vuetifyjs.com/en/components/ratings/ -->
      <v-container fluid id="view-area">
        <!-- Vew Goal Title -->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="11">
            <h1 class="message-title">
              Tasks
              <!--         Add Board Dialog   -->
              <v-dialog v-model="addBoardDialog" width="400">
                <template v-slot:activator="{ on, attrs }">
                  <span v-bind="attrs" v-on="on"
                    ><v-btn
                      depressed
                      small
                      rounded
                      color="#4465c0"
                      style="color: #f0f0f0;"
                      >Board +</v-btn
                    ></span
                  >
                </template>
                <v-card style="border-radius: 25px; padding: 20px;">
                  <v-card-title style="font-weight: 500;"
                    >Borad Title & Color</v-card-title
                  >

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12">
                          <v-text-field
                            label="Title*"
                            required
                            v-model="boardTitle"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="12">
                          <v-color-picker
                            v-model="showColor"
                            show-swatches
                            flat
                          ></v-color-picker>
                        </v-col>
                      </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn color="red" text @click="addBoardDialog = false"
                      >Cancel</v-btn
                    >

                    <!-- Add Board -->
                    <v-btn
                      color="blue"
                      text
                      @click="
                        addBoardDialog = false;
                        addBoard(boardTitle, showColor);
                      "
                      >OK</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </h1>
          </v-col>
        </v-row>

        <!-- -----------------------     -------------------- -->
        <!--                      Kanban                      -->
        <!-- -----------------------     -------------------- -->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="12">
            <div class="scrolling-wrapper">
              <div v-for="(board, index) in Boards.boards" :key="board.id">
                <div class="board-wrapper">
                  <h2 class="board-title">
                    <div
                      @click.stop="clickBoardTitle(board, index)"
                      style="display: inline; cursor: pointer;"
                    >
                      {{ board.board_title }}
                    </div>
                    <div
                      class="add-item-button"
                      :style="{ color: board.color }"
                      style="cursor: pointer;"
                    >
                      +
                    </div>
                  </h2>
                  <div class="board" :style="boardColor(index)">
                    <!-- Task Draggable -->
                    <draggable
                      v-model="board.tasks"
                      group="myGroup"
                      @start="drag = true"
                      @end="drag = false"
                      :options="options"
                    >
                      <div
                        @click="showDialog(task)"
                        class="item"
                        v-for="task in board.tasks"
                        :key="task.id"
                      >
                        <p class="text_position">
                          {{ task.task_title }}
                        </p>
                        <template v-if="task.is_repeat">
                          <v-chip small color="gray">
                            <v-icon>loop</v-icon>Repeat
                          </v-chip>
                        </template>
                      </div>
                    </draggable>
                  </div>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>

        <!--   Edit Board Dialog       -->
        <v-dialog v-model="editBoardDialog" width="400">
          <v-card style="border-radius: 25px; padding: 20px;">
            <v-btn icon color="#B6B6B6" @click="deleteBoardPopup = true">
              <v-icon>delete</v-icon>
            </v-btn>

            <v-card-title style="font-weight: 500;"
              >Change Borad Title & Color</v-card-title
            >
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      label="Title*"
                      required
                      v-model="currentBoard.board_title"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12">
                    <v-color-picker
                      show-swatches
                      flat
                      v-model="currentBoard.color"
                    ></v-color-picker>
                  </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="red" text @click="editBoardDialog = false"
                >Cancel</v-btn
              >

              <!-- Application of the change -->
              <v-btn
                color="blue"
                text
                @click="
                  editBoardDialog = false;
                  editBoard(
                    currentBoard.board_title,
                    currentBoard.color,
                    currentBoard.id,
                    currentIndex
                  );
                "
                >OK</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>

      <v-dialog v-model="deleteBoardPopup" max-width="290">
        <v-card>
          <v-card-title class="headline"
            >Delete "{{ currentBoard.board_title }} ?"</v-card-title
          >

          <v-card-text>
            Tasks that belong to "{{ currentBoard.board_title }}" will not be
            deleted. They will be assigned to "Unattached".
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
              color="green darken-1"
              text
              @click="deleteBoardPopup = false"
            >
              Cancel
            </v-btn>

            <v-btn
              color="red"
              text
              @click="
                deleteBoard(
                  currentBoard.board_title,
                  currentBoard.id,
                  currentIndex
                )
              "
            >
              Delete
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <div class="text-xs-center">
        <Task :text="text" ref="task"></Task>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import Task from "./Task";
import api from "@/services/api";

export default {
  name: "Goal",
  props: ["Boards"],
  name: "dnd",
  components: { draggable, Task },
  data() {
    return {
      // each dialog
      dialog: false,
      addBoardDialog: false,
      editBoardDialog: false,
      deleteBoardPopup: false,

      // add dialog data
      boardTitle: "",
      showColor: "#4465c0",

      // edit dialog data
      currentBoard: {},
      currentIndex: "",

      isClick: false,
      nowViewTask: "",

      // draggable data
      options: {
        group: "boardGroup",
        animation: 200
      },
      options: {
        group: "myGroup",
        animation: 200
      }
    };
  },
  methods: {
    // task dialog
    showDialog(item) {
      this.$refs.task.open();
      this.$refs.task.task_info = item;
      // Deep copy
      this.$refs.task.OriginalTaskInfo = JSON.parse(JSON.stringify(item));
    },
    // dynamic background
    boardColor(index) {
      const color = this.Boards.boards[index].color;
      if (color.slice(0, 1) == "#") {
        return `background: ${this.Boards.boards[index].color}`;
      } else {
        return `background: #${this.Boards.boards[index].color}`;
      }
    },
    addBoard(title, color) {
      const vm = this;
      let goalId = this.$route.params.id;
      api
        .post(
          `goals/${goalId}/boards/`,
          {
            goal: goalId,
            board_title: title,
            color: color
          },
          { useCredentails: true }
        )
        .then(function (response) {
          vm.Boards.boards.push(response.data);
          vm.editBoardDialog = false;
          // initialize input form
          vm.boardTitle = "";
          vm.showColor = "#4465c0";
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    deleteBoard(title, id, index) {
      const vm = this;
      let goalId = this.$route.params.id;
      api.delete(`goals/${goalId}/boards/${id}/`).then(function (res) {
        console.log(res);
        vm.deleteBoardPopup = false;
        vm.editBoardDialog = false;
        vm.Boards.boards.splice(index, 1);
      });
    },

    editBoard(title, color, id, index) {
      const vm = this;
      let goalId = this.$route.params.id;
      api
        .patch(
          `goals/${goalId}/boards/${id}/`,
          {
            board_title: title,
            color: color
          },
          { useCredentails: true }
        )
        .then(function (response) {
          // Overwrite the data in the changed part.
          // Use `splice` to reflect it immediately.
          vm.Boards.boards.splice(index, 1, response.data);
          vm.editBoardDialog = false;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    // In order to define `v-dialog` outside of `v-for`, you copy the whole data and use it.
    clickBoardTitle(board, index) {
      this.$set(this.currentBoard, "board_title", board.board_title);
      this.$set(this.currentBoard, "color", board.color);
      this.$set(this.currentBoard, "id", board.board_id);
      this.currentIndex = index;
      this.editBoardDialog = true;
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  /* adjust white space of Kanban to other component. */
  grid-template-columns: 100%;
  grid-template-areas: " view";
  background-color: #f0f0f0;
  position: relative;
}

#view-area {
  grid-area: view;
  overflow: hidden;
  position: relative;
}

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #4465c0;
}

.category-title {
  font-family: Roboto;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #ebebeb;
  padding-bottom: 15px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}

.content-splitter {
  border-block-end: solid 1px #c5c5c5;
}

/*  */
/*  */
.scrolling-wrapper {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  position: relative;
}

::-webkit-scrollbar {
  display: none;
  -webkit-appearance: none;
}

.board-wrapper {
  position: relative;
}

.board {
  flex: 0 0 auto;
  overflow: scroll;
  height: 500px;
  width: 300px;
  margin: 20px;
  position: relative;
  background: #4465c0;
  padding: 0px 0px;
  border-radius: 25px;
  box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
}

.board-title {
  top: 0px;
  margin-left: auto;
  margin-right: auto;
  padding-top: 20px;

  font-family: Roboto;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #444444;
}

.item {
  position: relative;
  /* border: solid purple 5px; */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.25);
  margin: 20px 15px;
  padding: 20px;
  border-radius: 25px;
  background: #f0f0f0;
}

.item:hover {
  cursor: grab;
}
.item:active {
  cursor: grabbing;
}

.text_position {
  font-size: 18px;
  color: #292929;
  position: relative;
}

.task_status {
  line-height: 1em;
  padding-left: 50px;
  position: absolute;
  bottom: 5px;
  right: 20px;
}
.add-item-button {
  display: inline;
  font-size: 28px;
  font-weight: 500;
}

/* -------------   --------------- */
/*           Over lay            */
/* -------------   --------------- */
.overlay-back {
  background: #f0f0f0;
  width: 1200px;
  border-radius: 50px;
  padding: 40px 60px;
  position: relative;
}

.delete-message {
  font-size: 14px;
  color: #b6b6b6;
}

@media only screen and (max-width: 600px) {
  .message-title {
    font-size: 30px;
    line-height: 56px;
  }
  .board {
    height: 450px;
    width: 270px;
    margin: 15px;
  }
  .text_position {
    font-size: 16px;
  }
  .item {
    padding: 15px;
    margin: 20px 15px;
  }
}
</style>
