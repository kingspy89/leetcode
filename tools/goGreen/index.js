import jsonfile from "jsonfile";
import moment from "moment";
import simpleGit from "simple-git";
import random from "random";

const path = "./data.json";

const makeCommits = (n) => {
  if (n === 0) return simpleGit().push();

  // Set fixed year 2025 and month November (10 zero indexed)
  const baseYear = 2025;
  const baseMonth = 10; // November
  // Random day between 1 and 22 (inclusive)
  const randomDay = random.int(1, 22);
  const randomHour = random.int(0, 23);

  const date = moment()
    .year(baseYear)
    .month(baseMonth)
    .date(randomDay)
    .hour(randomHour)
    .minute(0)
    .second(0)
    .format();

  const data = {
    date: date,
  };

  console.log(date);
  jsonfile.writeFile(path, data, () => {
    simpleGit().add([path]).commit(date, { "--date": date }, makeCommits.bind(this, --n));
  });
};

makeCommits(5);
